This plugin can be set from Faraday's Plugin Configuration, where the information of the BeEF's server and RESTful AuthKey
[AuthKey]  
[Host]  

By default this plugin is disabled, change the enable boolean in order to use it

The information required for connecting to BeEF is generated when you start beef:

    # ./beef 
    [21:03:58][*] Bind socket [imapeudora1] listening on [0.0.0.0:2000].
    [21:03:58][*] Browser Exploitation Framework (BeEF) 0.4.4.5-alpha
    [21:03:58]    |   Twit: @beefproject
    [21:03:58]    |   Site: http://beefproject.com
    [21:03:58]    |   Blog: http://blog.beefproject.com
    [21:03:58]    |_  Wiki: https://github.com/beefproject/beef/wiki
    [21:03:58][*] Project Creator: Wade Alcorn (@WadeAlcorn)
    [21:03:59][*] BeEF is loading. Wait a few seconds...
    [21:03:59][*] 10 extensions enabled.
    [21:03:59][*] 171 modules enabled.
    [21:03:59][*] 2 network interfaces were detected.
    [21:03:59][+] running on network interface: 127.0.0.1
    [21:03:59]    |   Hook URL: http://127.0.0.1:3000/hook.js
    [21:03:59]    |_  UI URL:   http://127.0.0.1:3000/ui/panel
    [21:03:59][+] running on network interface: 192.168.1.37
    [21:03:59]    |   Hook URL: http://192.168.1.37:3000/hook.js
    [21:03:59]    |_  UI URL:   http://192.168.1.37:3000/ui/panel
    [21:03:59][*] RESTful API key: 95e7923020559726d0b43deb1fc78c7dad09b75f
    [21:03:59][*] HTTP Proxy: http://127.0.0.1:6789
    [21:03:59][*] BeEF server started (press control+c to stop)
