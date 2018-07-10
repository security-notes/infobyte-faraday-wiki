
## ZSH web console

[- Commercial version -](https://www.faradaysec.com/#download)

It's also possible to use the ZSH interface inside your web browser. The idea of the web-shell is to allow you to work directly from the web using ZSH as a console. You would be connected to your own shell (listening in loopback interface).

To do this, fist you need to install butterfly:

```
$ pip install --user butterfly
```

NOTE: If you have both python2 and python3 in your system, it's better to use pip2 instead of pip.

Now, run butterfly:

```
$ butterfly.server.py --unsecure --shell=/bin/zsh --cmd="path/to/faraday/faraday-terminal.zsh [host] [port]"
```

Of course, you need to set the path of the folder in which you have Faraday (the [faraday-terminal.zsh](/faraday-terminal.zsh) script should be in the root of that folder) and pass the host and port arguments to that script, in case you've changed the Faraday's REST API parameters (remember that you have to run Faraday GTK or Faraday `--gui=no-gui` so that the terminal for ZSH functions properly).

Now, open a new tab from the web-shell icon in the web UI's sidebar, and you should see the zsh shell up and running!

![](https://raw.github.com/wiki/infobyte/faraday/images/client/webshell.png)
