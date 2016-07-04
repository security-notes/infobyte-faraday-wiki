Using the Debug button will launch an interactive ipython terminal for you to check on live objects.

![](https://raw.github.com/wiki/infobyte/faraday/images/Debug_button.png)

By default Debug button is disable to enable you to execute faraday in debug mode:
```
$ ./faraday -d 
```
To list the available objects just run

    > locals()
    self': <gui.qt3.mainwindow.MainWindow>

MainWindow is the main application context. 

You can ask for the ModelController to see the available hosts and interact with them:

    > self._model_controller.getAllHosts()