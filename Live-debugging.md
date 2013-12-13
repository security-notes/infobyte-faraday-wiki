Using the Debug button will launch an interactive ipython[0] terminal for you to check on live objects.

To list the available objects just run

    > locals()
self': <gui.qt3.mainwindow.MainWindow>

MainWindow is the main application context. You can ask for the ModelController to see the available hosts and interact with them:

    > self._model_controller.getAllHosts()