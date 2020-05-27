Faraday Addon is a simple addon for automate reporting vulnerabilities from the browser to your own Faraday instance. Faraday Addon intercepts every single request from the browser, adding a functionality for accessing each one of them and treating them as a vulnerability. In this way, a pentester only has to use the addon to send potential vulnerables requests to Faraday, instead of copy-paste them into the server.

## Compatibility
For the moment, Faraday Addon is only available for Firefox Quantum. We are working for an stable Chrome release.

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_addon/firefox-icon.png)

## Installation

### For Users
Download and install the last release from Firefox addons repository:

[Faraday Addon](https://addons.mozilla.org/es/firefox/addon/faraday-addon/)

### For Developers
$ git clone --depth 1 https://github.com/infobyte/faraday_addon.git



* On Firefox searchbox, write about:debugging.
* Click this button: Load Temporary Add-on
* Select the manifest.json file within the directory you cloned Faraday Addon.


## Getting Started!

At first, you must authenticate to your Faraday Server.

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_addon/dashboard.png)

Once logged in, go to Faraday Addon settings by clicking on its button and then on the settings button.

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_addon/button_without_workspace.png)

Now add Faraday Server's URL and click on Connect. (The URL must have this format **[protocol]://[ip/domain]:[port]**). If your settings are right, you should see your workspaces. Click the workspace you want and save your settings.

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_addon/configuration.png)

Faraday Addon also allows you to set scopes using regular expressions, thus allowing you to capture certain requests. For example, if you only want to capture every _faradaysec.com_ subdomains:

    *.faradaysec.com

Now you are ready for capturing requests with Faraday Addon.

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_addon/button_with_workspace.png)

## Adding a vulnerability to Faraday

If you have configured everything OK, you will see every request going through Faraday Addon. Imagine that you found a XSS and you want to send it to Faraday. To create a new issue, click on the icon next to the vulnerable request:

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_addon/button_requests.png)

A form will pop up, where you should complete it with all the information about the issue. If you have **Vulnerability Templates** previously uploaded to Faraday, this process will be faster.

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_addon/creating_vuln.png)

Once completed, send it to Faraday.

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_addon/requests.png)

You can check Faraday Server in order to see your new vulnerability.

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_addon/dashboard_2.png)
