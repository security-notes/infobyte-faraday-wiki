### Regular QT

Faraday main window is simple:  
![](https://raw.github.com/wiki/infobyte/faraday/images/Faraday-Mainwindow.png)

Structured in panes: Main Console, HostTree, Log Console, Item Info & Editing panes.

#### Auth
[- Commercial version -](https://www.faradaysec.com/#download)

If you are able to run Faraday QT with credentials add a login option

```
./faraday.pyc --login
```

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_guiqt_login.png)

Every command that you execute is intercepted and a handler is invoked in order to transparently import the newly generated information by the tool in the context of the pentest like ip addresses, hostnames, services, vulnerabilities, websites, notes, etc.