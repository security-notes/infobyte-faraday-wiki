This plugin allows a user to import all information about hosts, interfaces and specially vulnerabilities included in Client Side or Server Side attacks using Immunitys Canvas.

This plugin is a little different from the others, Immunity Canvas is the executor of this and not Faraday which makes it interesting to explain how to install it and how it works.

The installation is simple, copy the folder “faraday_report” located in

[Faraday_Installation]/helpers/plugins/canvas/ 

to the folder 

[Canvas_Installation]/exploits/reporting/

That’s all you need to do!

### How it works
In Canvas, open the module “faraday_report”, in the interface and you need to complete three fields:

1. Pickle file : This is the Canvas report, located in [Canvas_Installation]/Sessions/$SESSION_NAME
2. Report type: “clientd” for Client Side attacks or “Canvas” if not.
3. Input the “URL to XML RPC Faraday API”: If you didn’t change it, don't touch anything.

If you need more information about the installation or use of this plugin, look at this video: 
[Canvas Plugin](https://www.youtube.com/watch?v=MBFiT__y9iQ)