## Cli

It's possible to use Faraday in Command-Line Interface (CLI) mode, allowing you to process your reports in batch. So lets say you want to process the XML output of an **nmap** scan located in ```/tmp/nmap_scan.xml``` and send the results to a workspace called **project_one**. The way to do it using CLI mode would be to run:

```
$ faraday-client --cli --workspace project_one --report /tmp/nmap_scan.xml
```

NOTE: the workspace has to already exist for the command to work.

#### Professional and corporate versions

If you're using a professional or corporate version, you'll probably need to run Faraday as a certain user, with permissions to access your workspaces. You can pass your credentials using a simple json file the contains both your username and password. You have a template in the directory of your Faraday installation called `credentials.json`, but you are allowed to use any path and filename for this json file. The structure is this:

```
{
    "username": "your_user_here",
    "password": "your_password_here"
}
```

And then run Faraday:

```
$ faraday-client --cli --workspace project_one --report /tmp/nmap_scan.xml --creds-file /path/to/file/creds.json
```

***
<a name="zsh-web"></a>
