This wiki will help you to learn the different ways that Faraday has to import a report.

## Through the Web UI.

Go to the tab **Status Report** and click on the button --, then click on Select File button -- then upload the report.

## Through GTK Client
### Report Button

If you wish to add a report from a previous scan, you can do it from the GTK Client.

To do so, click on the Report Button and a dialog will open, from which you can select the tool that was used to generate the Report:

![](/home/javier/importing_report-2018-06-19_13.40.12.mp4)

Once you click OK, select the file you want to import and all the data in the report will be processed and added to the active Workspace, and the console will show a message when the plugin starts and ends.

## Through ZSH UI

To import your reports, drag-and-drop them into:

    $ ~/.faraday/report/[workspace_name]

Replace [workspace_name] with the workspace's name you're working in.
Faraday will parse your reports and upload the information extracted from them.

## Through CLI

It's possible to use Faraday in Command-Line Interface (CLI) mode, allowing you to process your reports in batch. So lets say you want to process the XML output of an nmap scan located in **/tmp/nmap_scan.xml** and send the results to a workspace called **project_one**. The way to do it using CLI mode would be to run:

    $ ./faraday.py --cli --workspace project_one --report /tmp/nmap_scan.xml

### Professional and corporate versions:

If you're using a professional or corporate version, you'll probably need to run Faraday as a certain user, with permissions to access your workspaces. You can pass your credentials using a simple json file the contains both your username and password. You have a template in the directory of your Faraday installation called credentials.json, but you are allowed to use any path and filename for this json file. The structure is this:

    {
        "username": "your_user_here",
        "password": "your_password_here"
    }


And then run Faraday:

    $ ./faraday.py --cli --workspace project_one --report /tmp/nmap_scan.xml --creds-file /path/to/file/credentials.json

## Through the API

In order to see information about uploading a report through the API, follow this link.