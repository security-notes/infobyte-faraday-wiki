This wiki will help you to learn the different ways that Faraday has to import a report.

### Through the Web UI.

* Go to the tab **Status Report** and click on the button:  ![](https://raw.github.com/wiki/infobyte/faraday/images/status_report/upload_report.png)
* Click on **Select File** in order to select the report that you are going to upload.
* Once you have selected the report, click on **Upload File** and your file will be uploaded.

### Through Faraday Client
_Faraday Client must be running in each case._

#### GTK Client

If you wish to add a report from a previous scan, you can do it also from the GTK Client.

To do so, click on the Report Button and a dialog will open, from which you can select the tool that was used to generate the Report:

![](https://raw.github.com/wiki/infobyte/faraday/images/status_report/upload_report_GTK.gif)

Once you click OK, select the file you want to import and all the data in the report will be processed and added to the active workspace, and the console will show a message when the plugin starts and ends.

#### Import multiple reports

To import your reports, drag-and-drop them into:

    $ /home/faraday/.faraday/report/[workspace_name]

Replace [workspace_name] with the workspace's name you're working in.
Faraday will parse your reports and upload the information extracted from them.

If the client has problems detecting the plugin that should parse the report,
you should change the report filename by adding `_faraday_PLUGINNAME` just before
the extension. For example, if you have an Openvas plugin called `myreport.xml` and
it isn't detected correctly, rename it to `myreport_faraday_Openvas.xml`.

***Note:*** The plugin name must be one that appears in the plugin list that
is showed when you click on "Import report" in the GTK client:
![](https://raw.github.com/wiki/infobyte/faraday/images/client/plugin_names.png)
**Remember that it is case sensitive**.


#### CLI (Community)

It's possible to use Faraday in Command-Line Interface (CLI) mode, allowing you to process your reports in batch. So lets say you want to process the XML output of an nmap scan located in **/tmp/nmap_scan.xml** and send the results to a workspace called **project_one**. The way to do it using CLI mode would be to run:

    $ faraday-client --cli --workspace project_one --report /tmp/nmap_scan.xml

#### CLI (Professional and Corporate versions)

If you're using a Professional or Corporate version, you'll probably need to run Faraday as a certain user, with permissions to access your workspaces. You can pass your credentials using a simple json file that contains both your username and password. You have a template in the directory of your Faraday installation called credentials.json, but you are allowed to use any path and filename for this json file. The structure is this:

    {
        "username": "your_user_here",
        "password": "your_password_here"
    }


And then run Faraday:

    $ faraday-client --cli --workspace project_one --report /tmp/nmap_scan.xml --creds-file /path/to/file/credentials.json

### Through the API

In order to see information about uploading a report through the API, follow this [link](https://github.com/infobyte/faraday/wiki/API-Server#examples).
