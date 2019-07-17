This plugin is a script developed in Java as a extender to the Burp Proxy API (Pro/Community).

### Installation

To download Faraday's Burp extension, follow this [link](https://github.com/infobyte/faraday/releases/download/v3.8.0/faraday-burp-v2.0.1.jar)

Once you have downloaded the extension, follow these steps:

* Go to Extender->Extensions and click in the Add button.

* In the Extension Details section, the extension type should be **Java**, and the extension file should be the path to the faraday-burp-plugin-v2.jar file that you downloaded above. 

![](https://raw.github.com/wiki/infobyte/faraday/images/plugins/burp/add_extension.png)

* Click Next, and if everything went well, you should see no errors and you can close the window.

* Now, make sure the extension is loaded in the Extensions tab.

![](https://raw.github.com/wiki/infobyte/faraday/images/plugins/burp/loaded.png)

### Configuration options

Once the Faraday extension is loaded into your Burp, you will see a new tab called "Faraday".

![](https://raw.github.com/wiki/infobyte/faraday/images/plugins/burp/configuration.png)

Here, you can login to Faraday and you can edit the extension's settings:

#### Login to Faraday

In order to connect the Faraday's Burp extension to Faraday, follow these steps:

1) Set your Faraday Server URL. This should point to the same URL that you use when you are connecting to Faraday Server, e.g: http://127.0.0.1:5985

2) Connect Burp to Faraday by clicking on the **Connect** button.

![](https://raw.github.com/wiki/infobyte/faraday/images/plugins/burp/configuration_connected.png)

3) Once you are connected, type your Faraday's credentials: username, password and 2FA Token (if it is the case).

4) Login into Faraday by click on the **Login** button. If everything goes well, Burp should pop up a _Login successful!_ modal. 

![](https://raw.github.com/wiki/infobyte/faraday/images/plugins/burp/configuration_login_success.png)

![](https://raw.github.com/wiki/infobyte/faraday/images/plugins/burp/configuration_logged_in.png)

5) Once you are logged in, you can edit the extension's settings.

#### Extension Settings

![](https://raw.github.com/wiki/infobyte/faraday/images/plugins/burp/extension_settings.png)

From here, you can:

1) Choose the workspace where you want to work on.

2) Choose whether the vulnerabilities should be imported automatically or not (it's disabled by default).

3) Import the vulnerabilities you've found so far.

4) Check if you want to use only Burp scope.

#### Other Settings

![](https://raw.github.com/wiki/infobyte/faraday/images/plugins/burp/other_settings.png)

From here, you can Restore Settings to default.

### Send to Faraday

Once you have everything setup, you can send the issues or requests to Faraday.

![](https://raw.github.com/wiki/infobyte/faraday/images/plugins/burp/send_to.png)


