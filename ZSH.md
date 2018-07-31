***
### ZSH UI

You can even run Faraday in detached mode connecting with a ZSH terminal to it:

First, you need to run Faraday with no GUI:

``` 
    $ python faraday.py --gui=no-gui
```

![](https://raw.github.com/wiki/infobyte/faraday/images/client/no-ui.png)

Now, run Faraday Terminal:

```
    $ ./faraday-terminal.zsh
```

![](https://raw.github.com/wiki/infobyte/faraday/images/client/no-ui2.png)

To import your reports, drag-and-drop them into:

    $ ~/.faraday/uploaded_reports/[workspace_name]

Replace [workspace_name] with the workspace's name you're working in.

Faraday will parse your reports and upload the information extracted from them.