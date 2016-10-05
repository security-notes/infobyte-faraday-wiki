In order to update your Faraday version run:

```
./faraday.py --update
```

[- Commercial version -](https://www.faradaysec.com/#download)
### Commercial version update

1) Close all your instances of Faraday and Faraday Server.

2) Download the last tarball version from Faraday Customer Portal using the username and password you received after your purchase.

3) Unpack it in your new Faraday directory. 

4) If you have a to update also your license you have to copy and replace your files in the following directory $HOME/.faraday/doc/:

5) After doing that, run the following command to make sure all dependencies are met:

```
./setup_server.sh
```

5) Run faraday server: 

```
./faraday-server.pyc 
```

6) Run your Faraday Client:
```
./faraday.pyc --update --login
```

Following the same steps in every instance of Faraday

Now you're ready to go!