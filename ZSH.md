### ZSH UI

You can even run Faraday in detached mode connecting with a ZSH terminal to it:

First, you need to run Faraday with no GUI:

``` 
    $ faraday-client --gui=no-gui
```

![](https://raw.github.com/wiki/infobyte/faraday/images/client/no_ui.png)

Now, run Faraday Terminal:

```
    $ faraday-terminal
```

![](https://raw.github.com/wiki/infobyte/faraday/images/client/no_ui2.png)

### Using oh-my-zsh

You can use [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) for managing your ZSH configuration. All you need to do is to [install](https://github.com/robbyrussell/oh-my-zsh#basic-installation) oh-my-zsh framework and then run the faraday-terminal command.

### Importing your reports

To import your reports, drag-and-drop them into:

    $ /home/faraday/.faraday/reports/[workspace_name]

Replace [workspace_name] with the workspace's name you're working in.

Faraday will parse your reports and upload the information extracted from them.