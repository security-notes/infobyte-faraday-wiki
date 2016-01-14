Faraday has 3 different ways to interact with information:
* [GUI QT] (https://github.com/infobyte/faraday/wiki/Usage#gui-qt)
* [ZSH UI] (https://github.com/infobyte/faraday/wiki/Usage#running-with-zsh-ui)
* [Web UI] (https://github.com/infobyte/faraday/wiki/Web UI)

### GUI QT

Faraday main window is simple:  
![](https://raw.github.com/wiki/infobyte/faraday/images/Faraday-Mainwindow.png)

Structured in panes: Main Console, HostTree, Log Console, Item Info & Editing panes.

#### GUI QT with authentication
[- Commercial version -](https://www.faradaysec.com/#download)

If you are able to run Faraday QT with credentials add a login option

```
./faraday.pyc --login
```

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_guiqt_login.png)

Every command that you execute is intercepted and a handler is invoked in order to transparently import the newly generated information by the tool in the context of the pentest like ip addresses, hostnames, services, vulnerabilities, websites, notes, etc.

### Running with ZSH UI

You can even run Faraday in detached mode connecting with a ZSH terminal to it:

![](https://raw.github.com/wiki/infobyte/faraday/images/no-ui.png)
![](https://raw.github.com/wiki/infobyte/faraday/images/no-ui2.png)

No manual imports needed but supported. Just drop your fresh generated reports in:
    $ ~/.faraday/report/workspace_name

Faraday will parse your reports and upload the information extracted from them.

#### ZSH web console

[- Commercial version -](https://www.faradaysec.com/#download)

It's also possible to use the ZSH interface inside your web browser. To do this, fist you need to install butterfly:
```
$ pip install --user butterfly
```
NOTE: If you have both python2 and python3 in your system, it's better to use pip2 instead of pip.

Now, run butterfly:
```
$ butterfly.server.py --unsecure --shell=/bin/zsh --cmd="<path/of/faraday/>faraday-terminal.zsh [host] [port]"
```

Of course, you need to set the path of the folder in which you have faraday (the faraday-terminal.zsh script should be in the root of that folder). Also, You can pass the host and port as arguments to that script, in case you've changed the Faraday's REST API parameters (remember that you have to run Faraday QT or Faraday —gui=nogui so that the terminal for ZSH functions properly)

The idea of the webshell is to be able to do actions directly from the web using ZSH as a console. You would be connected to your own shell (listening in loopback interface). 

Then, open a new tab from the webshell icon in the web UI's sidebar, and you should see the zsh shell up and running!

![](https://raw.github.com/wiki/infobyte/faraday/images/butterfly_webshell.png)